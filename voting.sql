DROP DATABASE IF EXISTS blockchain_voting;

CREATE DATABASE blockchain_voting;

USE blockchain_voting;

-- =========================================
-- ELECTION COMMISSION VOTER DATABASE
-- =========================================

CREATE TABLE eligible_voters (
    aadhaar_no VARCHAR(12) PRIMARY KEY,
    voter_name VARCHAR(100) NOT NULL,
    constituency VARCHAR(100) NOT NULL
);

-- =========================================
-- TRACK WHO HAS ALREADY VOTED
-- =========================================

CREATE TABLE voted_voters (
    aadhaar_no VARCHAR(12) PRIMARY KEY,
    voted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================================
-- POLITICAL PARTIES
-- =========================================

CREATE TABLE parties (
    id INT AUTO_INCREMENT PRIMARY KEY,
    party_name VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO parties (party_name)
VALUES
('TDP'),
('YSRCP'),
('Jana Sena'),
('BJP'),
('Congress');

-- =========================================
-- BLOCKCHAIN VOTES
-- =========================================

CREATE TABLE blockchain_votes (
    id INT AUTO_INCREMENT PRIMARY KEY,

    aadhaar_no VARCHAR(12) NOT NULL,

    voter_name VARCHAR(100) NOT NULL,

    constituency VARCHAR(100) NOT NULL,

    party VARCHAR(100) NOT NULL,

    block_hash VARCHAR(64) NOT NULL,

    previous_hash VARCHAR(64) NOT NULL,

    timestamp DATETIME NOT NULL
);