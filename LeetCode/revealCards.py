def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        out = []
        out.append(deck[0])
        for i in range(1,len(deck)):
            m = out.pop()
            out.insert(0,m)
            out.insert(0,deck[i])
        return out
