# Blockchain Voting System

## Overview

The Andhra Pradesh Blockchain Voting System is a secure digital voting platform developed using Blockchain technology, Python, Streamlit, and MySQL.

The system allows eligible voters to cast their votes using their Aadhaar number after verification against the Election Commission voter database. Every vote is stored as a blockchain block, ensuring transparency, immutability, and security.

The project also provides constituency-wise election results, constituency winners, party-wise vote counts, and assembly seat calculations similar to a real Andhra Pradesh Legislative Assembly election.

---

## Features

### Voter Verification

* Aadhaar-based voter identification
* Verification against Election Commission voter database
* Displays voter details after successful verification
* Prevents unauthorized voting

### One Person – One Vote

* Tracks voters who have already voted
* Blocks duplicate voting attempts

### Blockchain Security

* Every vote is stored as a blockchain block
* SHA-256 hashing algorithm used
* Previous block hash linking ensures chain integrity
* Tamper-resistant vote storage

### Political Party Voting

Supported parties:

* Telugu Desam Party (TDP)
* Yuvajana Sramika Rythu Congress Party (YSRCP)
* Jana Sena Party
* Bharatiya Janata Party (BJP)
* Indian National Congress

### Constituency-Based Election System

* Supports all 175 Andhra Pradesh Assembly Constituencies
* Stores votes constituency-wise
* Calculates constituency-wise winners
* Calculates majority margins
* Calculates assembly seats won by each party

### Results Dashboard

* Party-wise vote count
* Constituency-wise vote count
* Constituency winners
* Assembly seat distribution
* Interactive charts and visualizations

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* MySQL

### Security

* Blockchain
* SHA-256 Hashing

---

## Project Architecture

Election Commission Database

↓

Aadhaar Verification

↓

Voter Authentication

↓

Party Selection

↓

Blockchain Vote Recording

↓

Constituency-wise Result Processing

↓

Assembly Seat Calculation

↓

Results Dashboard

---

## Database Schema

### eligible_voters

Stores Election Commission voter records.

| Column       | Type         |
| ------------ | ------------ |
| aadhaar_no   | VARCHAR(12)  |
| voter_name   | VARCHAR(100) |
| constituency | VARCHAR(100) |

### voted_voters

Stores voters who have already cast their vote.

| Column     | Type        |
| ---------- | ----------- |
| aadhaar_no | VARCHAR(12) |
| voted_at   | TIMESTAMP   |

### parties

Stores participating political parties.

| Column     | Type         |
| ---------- | ------------ |
| id         | INT          |
| party_name | VARCHAR(100) |

### blockchain_votes

Stores blockchain vote records.

| Column        | Type         |
| ------------- | ------------ |
| aadhaar_no    | VARCHAR(12)  |
| voter_name    | VARCHAR(100) |
| constituency  | VARCHAR(100) |
| party         | VARCHAR(100) |
| block_hash    | VARCHAR(64)  |
| previous_hash | VARCHAR(64)  |
| timestamp     | DATETIME     |

---

## Blockchain Structure

Each vote generates a block containing:

* Aadhaar Number
* Voter Name
* Constituency
* Selected Party
* Previous Hash
* Current Hash
* Timestamp

Hash Generation:

SHA-256(
aadhaar +
voter_name +
constituency +
party +
previous_hash +
timestamp
)

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd blockchain_voting
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Create MySQL database:

```sql
CREATE DATABASE blockchain_voting;
```

Import schema:

```bash
mysql -u root -p blockchain_voting < schema.sql
```

### Configure Database Credentials

Update `config.py`:

```python
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_password"
MYSQL_DATABASE = "blockchain_voting"
```

### Run Application

```bash
streamlit run app.py
```

---

## Testing

Sample Aadhaar Numbers:

* 100000000001
* 100000000002
* 100000000003
* 100000000004
* 100000000005

Use these records from the `eligible_voters` table to test the application.

---

## Future Enhancements

* Facial Recognition Verification
* OTP Authentication
* Digital Signature Verification
* Ethereum Smart Contract Integration
* Distributed Blockchain Network
* Real-Time Election Analytics
* Mobile Application Support
* Cloud Deployment

---

## Advantages

* Transparent voting process
* Secure vote storage
* Prevention of duplicate voting
* Tamper-resistant blockchain records
* Constituency-wise election management
* Real-time result generation
* Scalable architecture

---

## Educational Purpose

This project was developed as an academic project to demonstrate the integration of Blockchain Technology with Digital Voting Systems and Election Management Processes.

---

## License

This project is intended for educational and research purposes.
