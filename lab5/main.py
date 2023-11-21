from server import Server
from client import Client
from vote import VOTE

def main():
    server = Server()
    
    client = Client(server, 'Alice')
    client.vote(VOTE.YES)
    
    client = Client(server, 'Bob')
    client.vote(VOTE.YES)
    
    client = Client(server, 'Tom')
    client.vote(VOTE.NO)
    
    client = Client(server, 'Rahman')
    client.vote(VOTE.YES)
    
    server.voting_results()
    
    client = Client(server, 'Zamir')
    client.vote(VOTE.ABSTAIN)
    
    client = Client(server, 'Dugar')
    client.vote(VOTE.ABSTAIN)
    
    client = Client(server, 'Sasha')
    client.vote(VOTE.ABSTAIN)
    
    server.voting_results()
    
if __name__ == "__main__":
    main()