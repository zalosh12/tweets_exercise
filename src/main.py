from manager import Manager

def main():
    manager = Manager(r"../data/tweets_dataset.csv")
    manager.run()

if __name__  == "__main__":
    main()

