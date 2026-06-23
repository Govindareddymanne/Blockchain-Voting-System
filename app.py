# app.py

import streamlit as st
import os

from blockchain import Block

from db import (
    get_voter_details,
    voter_exists,
    mark_voted,
    save_block,
    get_last_hash,
    get_party_results,
    get_constituency_results
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AP Blockchain Voting System",
    layout="wide"
)

# ==========================================
# PARTY IMAGES
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

parties = [
    (
        "TDP",
        os.path.join(BASE_DIR, "images", "tdp.png")
    ),
    (
        "YSRCP",
        os.path.join(BASE_DIR, "images", "ysrcp.png")
    ),
    (
        "Jana Sena",
        os.path.join(BASE_DIR, "images", "janasena.png")
    ),
    (
        "BJP",
        os.path.join(BASE_DIR, "images", "bjp.png")
    ),
    (
        "Congress",
        os.path.join(BASE_DIR, "images", "congress.png")
    )
]

# ==========================================
# TITLE
# ==========================================

st.title(
    "🗳️ Andhra Pradesh Blockchain Voting System"
)

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Vote",
        "Results"
    ]
)

# ==========================================
# VOTE PAGE
# ==========================================

if menu == "Vote":

    st.header("Cast Your Vote")

    aadhaar_no = st.text_input(
        "Enter Aadhaar Number",
        max_chars=12
    )

    voter_name = None
    constituency = None

    if len(aadhaar_no) == 12:

        voter = get_voter_details(
            aadhaar_no
        )

        if voter is None:

            st.error(
                "Aadhaar not found in Election Commission Database"
            )

        else:

            voter_name, constituency = voter

            st.success(
                "Voter Verified Successfully"
            )

            st.write(
                f"Name : {voter_name}"
            )

            st.write(
                f"Constituency : {constituency}"
            )

            if voter_exists(
                aadhaar_no
            ):

                st.error(
                    "You have already voted"
                )

            else:

                st.subheader(
                    "Select Your Party"
                )

                cols = st.columns(5)

                for i, (party, image_path) in enumerate(parties):

                    with cols[i]:

                        st.image(
                            image_path,
                            width=120
                        )

                        st.markdown(
                            f"""
                            <h4 style='text-align:center'>
                            {party}
                            </h4>
                            """,
                            unsafe_allow_html=True
                        )

                        if st.button(
                            f"Vote {party}",
                            key=party
                        ):

                            previous_hash = (
                                get_last_hash()
                            )

                            block = Block(
                                aadhaar_no,
                                voter_name,
                                constituency,
                                party,
                                previous_hash
                            )

                            save_block(
                                aadhaar_no,
                                voter_name,
                                constituency,
                                party,
                                block.hash,
                                previous_hash,
                                block.timestamp
                            )

                            mark_voted(
                                aadhaar_no
                            )

                            st.success(
                                f"✅ Vote Cast Successfully For {party}"
                            )

                            st.write(
                                "Blockchain Hash"
                            )

                            st.code(
                                block.hash
                            )

# ==========================================
# RESULTS PAGE
# ==========================================

elif menu == "Results":

    st.header(
        "Election Results"
    )

    # --------------------------------------
    # PARTY WISE VOTES
    # --------------------------------------

    st.subheader(
        "Party Wise Vote Count"
    )

    party_results = (
        get_party_results()
    )

    chart_data = {}

    for party, votes in party_results:

        st.metric(
            party,
            votes
        )

        chart_data[
            party
        ] = votes

    st.bar_chart(
        chart_data
    )

    # --------------------------------------
    # CONSTITUENCY RESULTS
    # --------------------------------------

    st.subheader(
        "Constituency Wise Results"
    )

    constituency_results = (
        get_constituency_results()
    )

    for constituency, party, votes in constituency_results:

        st.write(
            f"{constituency} | {party} | {votes}"
        )

    # --------------------------------------
    # CONSTITUENCY WINNERS
    # --------------------------------------

    st.subheader(
        "Constituency Winners"
    )

    winners = {}

    for constituency, party, votes in constituency_results:

        if (
            constituency not in winners
            or votes > winners[constituency][1]
        ):

            winners[
                constituency
            ] = (
                party,
                votes
            )

    for constituency, data in winners.items():

        party = data[0]
        votes = data[1]

        st.success(
            f"{constituency} → {party} ({votes} votes)"
        )

    # --------------------------------------
    # ASSEMBLY SEATS WON
    # --------------------------------------

    st.subheader(
        "Assembly Seats Won"
    )

    seat_count = {}

    for constituency, data in winners.items():

        party = data[0]

        seat_count[
            party
        ] = seat_count.get(
            party,
            0
        ) + 1

    for party, seats in seat_count.items():

        st.metric(
            party,
            seats
        )

    st.bar_chart(
        seat_count
    )