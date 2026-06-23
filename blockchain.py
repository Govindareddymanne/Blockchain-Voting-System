import hashlib
from datetime import datetime


class Block:

    def __init__(
        self,
        aadhaar_no,
        voter_name,
        constituency,
        party,
        previous_hash
    ):

        self.timestamp = str(datetime.now())

        self.aadhaar_no = aadhaar_no
        self.voter_name = voter_name
        self.constituency = constituency
        self.party = party
        self.previous_hash = previous_hash

        self.hash = self.generate_hash()

    def generate_hash(self):

        data = (
            self.aadhaar_no +
            self.voter_name +
            self.constituency +
            self.party +
            self.previous_hash +
            self.timestamp
        )

        return hashlib.sha256(
            data.encode()
        ).hexdigest()

    def to_dict(self):

        return {
            "aadhaar_no": self.aadhaar_no,
            "voter_name": self.voter_name,
            "constituency": self.constituency,
            "party": self.party,
            "previous_hash": self.previous_hash,
            "hash": self.hash,
            "timestamp": self.timestamp
        }