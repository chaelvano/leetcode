class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()

        count = 0

        n_players = len(players)
        n_trainers = len(trainers)

        p = 0
        t = 0

        while p < n_players and t < n_trainers:
            if players[p] <= trainers[t]:
                count += 1
                p += 1
                t += 1
            else:
                t += 1

        return count
