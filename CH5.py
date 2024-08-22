from cryptography.fernet import Fernet
import hashlib
import json

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# List to store encrypted votes
votes = []

# Function to encrypt and add a vote
def cast_vote(vote):
    # Encrypt the vote
    encrypted_vote = cipher_suite.encrypt(vote.encode())
    votes.append(encrypted_vote)

# Function to hash the vote
def hash_vote(vote):
    return hashlib.sha256(vote).hexdigest()

# Function to tally votes
def tally_votes():
    decrypted_votes = [cipher_suite.decrypt(vote).decode() for vote in votes]
    # Count votes (for simplicity, assuming votes are for 'Party X' or 'Party Y')
    results = {'Party X': 0, 'Party Y': 0}
    for vote in decrypted_votes:
        results[vote] += 1
    return results

# Main function to take user input and cast votes
def main():
    print("Welcome to the Electronic Voting System")
    print("Please vote for your preferred party:")
    print("1. Party X")
    print("2. Party Y")
    
    while True:
        choice = input("Enter your choice (1 or 2) or 'q' to quit: ")
        if choice == '1':
            cast_vote('Party X')
            print("You voted for Party X.")
        elif choice == '2':
            cast_vote('Party Y')
            print("You voted for Party Y.")
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

    print("\nVoting period has ended. Tallying votes...\n")
    results = tally_votes()
    print("Voting results:", results)

# Run the voting system
if __name__ == "__main__":
    main()
