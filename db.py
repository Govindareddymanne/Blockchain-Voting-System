import mysql.connector
from config import *


def get_connection():

    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )


# =====================================
# VOTER VERIFICATION
# =====================================

def get_voter_details(aadhaar_no):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            voter_name,
            constituency
        FROM eligible_voters
        WHERE aadhaar_no=%s
        """,
        (aadhaar_no,)
    )

    result = cur.fetchone()

    conn.close()

    return result


# =====================================
# CHECK ALREADY VOTED
# =====================================

def voter_exists(aadhaar_no):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM voted_voters
        WHERE aadhaar_no=%s
        """,
        (aadhaar_no,)
    )

    result = cur.fetchone()

    conn.close()

    return result is not None


# =====================================
# MARK AS VOTED
# =====================================

def mark_voted(aadhaar_no):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO voted_voters
        (aadhaar_no)
        VALUES(%s)
        """,
        (aadhaar_no,)
    )

    conn.commit()
    conn.close()


# =====================================
# SAVE BLOCKCHAIN VOTE
# =====================================

def save_block(
    aadhaar_no,
    voter_name,
    constituency,
    party,
    block_hash,
    previous_hash,
    timestamp
):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO blockchain_votes
        (
            aadhaar_no,
            voter_name,
            constituency,
            party,
            block_hash,
            previous_hash,
            timestamp
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            aadhaar_no,
            voter_name,
            constituency,
            party,
            block_hash,
            previous_hash,
            timestamp
        )
    )

    conn.commit()
    conn.close()


# =====================================
# GET LAST BLOCK HASH
# =====================================

def get_last_hash():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT block_hash
        FROM blockchain_votes
        ORDER BY id DESC
        LIMIT 1
        """
    )

    row = cur.fetchone()

    conn.close()

    if row:
        return row[0]

    return "0"


# =====================================
# PARTY WISE RESULTS
# =====================================

def get_party_results():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            party,
            COUNT(*) AS votes
        FROM blockchain_votes
        GROUP BY party
        ORDER BY votes DESC
        """
    )

    data = cur.fetchall()

    conn.close()

    return data


# =====================================
# CONSTITUENCY WISE RESULTS
# =====================================

def get_constituency_results():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            constituency,
            party,
            COUNT(*) AS votes
        FROM blockchain_votes
        GROUP BY constituency, party
        ORDER BY constituency, votes DESC
        """
    )

    data = cur.fetchall()

    conn.close()

    return data


# =====================================
# GET ALL PARTIES
# =====================================

def get_parties():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT party_name
        FROM parties
        """
    )

    data = cur.fetchall()

    conn.close()

    return [row[0] for row in data]