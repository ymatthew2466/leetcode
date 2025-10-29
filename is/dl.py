'''
We have a CD player that can hold several CDs at once.  Each CD has the same number of songs, though there may be many duplicates of the same song in our collection, or even on the same CD.  

The CD player always starts at the first CD in the list on the first song (song #0).  After each song, it shuffles to any other CD at random, but only moves forward or backward one song number (it will not move backward if on the first song, nor forward if on the last song).

Example 1 (cd_list0):
Song #  ->  0          1           2          3
            --------   --------    -------    --------
cd0       | Thriller   Thriller    Lights     Thriller
cd1       | Thriller   Royals      Lights     Thriller
cd2       | Thriller   Thriller    Vogue      Thriller

For instance, if Vogue (cd2, song #2) just played, the shuffle may move backward a song to Thriller or Royals (song #1 of cd0 or cd1) or forward a song to Thriller (song #3 of either cd0 or cd1).  On the other hand, if Thriller just played (cd0, song #0), it could only move to Royals, because its other possible move would move to a Thriller song.

Example 2 (cd_list1):
Song #  ->  0          1           2          3
            --------   --------    -------    --------
cd0       | Thriller   Thriller    Lights     Thriller
cd3       | Thriller   Royals      Thriller   Lights
cd2       | Thriller   Thriller    Vogue      Thriller

Write an algorithm that takes a list of CDs and returns any valid path that the shuffle function could take, with the cd and song number of each song, such that each unique song is played exactly once with no repetitions.  If it is not possible to form such a list, return an empty list.

cd_list0 = [cd0, cd1, cd2]
play_all_songs(cd_list0) => []
cd_list1 = [cd0, cd3, cd2]
play_all_songs(cd_list1) => [(0,0), (1,1), (2,2), (1,3)] (Thriller, Royals, Vogue, Lights)

Additional Input:
cd4 = ["Roar", "Superstition", "Roar"]
cd5 = ["Africa","Zombie", "Africa"]
cd6 = ["Push", "Happy", "Happy"] 
cd_list2 = [cd4, cd5, cd6]

cd7 = ["Survivor", "Survivor", "Yesterday", "Survivor",]
cd8 = ["Survivor", "Waterfalls", "Survivor", "Faith",]
cd9 = ["Faith", "Survivor", "Survivor", "Survivor",]
cd_list3 = [cd7, cd8, cd9]

cd10 = ["Mamma mia", "Yesterday"]
cd11 = ["Mamma mia", "Yesterday"]
cd12 = ["Yesterday", "Mamma mia"]
cd13 = ["Yesterday", "Mamma mia"]
cd_list4 = [cd11, cd10]
cd_list5 = [cd10, cd12]
cd_list6 = [cd10, cd12, cd11, cd13]

cd14 = ["Thriller", "Thriller", "Lights", "Thriller"]
cd15 = ["Thriller", "Royals", "Vogue", "Closing"]
cd_list7 = [cd14, cd15]

All Test Cases - snake_case:
play_all_songs(cd_list0) => []
play_all_songs(cd_list1) => [(0,0), (1,1), (2,2), (1,3)]
play_all_songs(cd_list2) => multiple options of length 6:
[(0, 0), (1, 1), (2, 0), (0, 1), (1, 0), (2, 1)] OR			
[(0, 0), (1, 1), (2, 0), (0, 1), (1, 2), (2, 1)] OR			
[(0, 0), (2, 1), (1, 0), (0, 1), (2, 0), (1, 1)] OR			
[(0, 0), (2, 1), (1, 2), (0, 1), (2, 0), (1, 1)]
play_all_songs(cd_list3) => [(0,0), (1,1), (0,2), (1,3)]	
play_all_songs(cd_list4) => [(0,0), (1,1)]
play_all_songs(cd_list5) => []
play_all_songs(cd_list6) => [(0,0), (2,1)]
play_all_songs(cd_list7) => []

All Test Cases - camelCase:
playAllSongs(cdList0) => []
playAllSongs(cdList1) => [(0,0), (1,1), (2,2), (1,3)]
playAllSongs(cdList2) => multiple options of length 6:
[(0, 0), (1, 1), (2, 0), (0, 1), (1, 0), (2, 1)] OR			
[(0, 0), (1, 1), (2, 0), (0, 1), (1, 2), (2, 1)] OR			
[(0, 0), (2, 1), (1, 0), (0, 1), (2, 0), (1, 1)] OR			
[(0, 0), (2, 1), (1, 2), (0, 1), (2, 0), (1, 1)]
playAllSongs(cdList3) => [(0,0), (1,1), (0,2), (1,3)]	
playAllSongs(cdList4) => [(0,0), (1,1)]
playAllSongs(cdList5) => []
playAllSongs(cdList6) => [(0,0), (2,1)]
playAllSongs(cdList7) => []

Complexity Variables:
C = the number of CDs
S = the number of songs per CD


=============


Example 1 (cd_list0):
Song #  ->  0          1           2          3
            --------   --------    -------    --------
cd0       | Thriller   Thriller    Lights     Thriller
cd1       | Thriller   Royals      Lights     Thriller
cd2       | Thriller   Thriller    Vogue      Thriller

visit set
order: []
def dfs(curr song):
    if song in visited:
        return False
    if len(set)==num songs:
        return True or order list
    
    visited.add(curr song)
    iterate thru ALL CDS:
        if curr cd: continue to skip
        left track, right track
        bounds check on tracks
        dfs(new cd, left:index)
        dfs(new cd, right:index)
    
    backtrack
    visited.remove(curr song)
    order.append(curr song)

Example 2 (cd_list1):
Song #  ->  0          1           2          3
            --------   --------    -------    --------
cd0       | Thriller   Thriller    Lights     Thriller
cd3       | Thriller   Royals      Thriller   Lights
cd2       | Thriller   Thriller    Vogue      Thriller

'''

def playAllSongs(cdList: []):
    # cdList = [[list], [list], [list]]
    # cdList[0] = song list of cd0
    indices = list(range(len(cdList)))  # list

    visited = set()
    order = []
    song_count = len(cdList)
    cdList_ints = indices

    def dfs(curr_cd: int, curr_song: int):
        
        # not a valid path (revisit)
        if curr_song in visited:
            return False
        # base case: visit all unique songs
        if len(visited) == song_count:
            return True
        
        # add THIS cd to visited (prevent dupes later)
        visited.add(curr_cd)
        
        # iterate thru cds
        for cd_index in cdList_ints:
            # print(f"currcd: {curr_cd}, currsong:{cd_index}, {cdList[curr_cd][cd_index]}")
            # can't look at curr cd
            if cd_index==curr_cd:
                continue
            left = cd_index-1
            left_song = cdList[curr_cd][left]
            # print(f"left: {left}, leftsong: {left_song}")
            right = cd_index+1
            right_song = cdList[curr_cd][right]
            # print(f"right: {right}, rightsong: {right_song}")
            # left cd
            if left>=0 and left<len(cdList) and left!=curr_song and curr_song!=left_song:
                if not dfs(cd_index, left):
                    continue
            # right cd
            if right>=0 and right<len(cdList) and right!=curr_song and curr_song!=right_song:
                if not dfs(cd_index, right):
                    continue
        
        print(f"curr_cd: {curr_cd}, curr_song: {curr_song}")
        # backtrack
        visited.remove(curr_cd)
        order.append(curr_cd)
        return True

    if dfs(0,0):
        return order
    else:
        return []
    
    






cd0 = ["Thriller", "Thriller", "Lights", "Thriller"]
cd1 = ["Thriller", "Royals", "Lights", "Thriller"]
cd2 = ["Thriller", "Thriller", "Vogue", "Thriller"]
cd3 = ["Thriller", "Royals", "Thriller", "Lights"]
cd_list0 = [cd0, cd1, cd2]
cd_list1 = [cd0, cd3, cd2]

print(playAllSongs(cd_list1))


cd4 = ["Roar", "Superstition", "Roar"]
cd5 = ["Africa","Zombie", "Africa"]
cd6 = ["Push", "Happy", "Happy"] 
cd_list2 = [cd4, cd5, cd6]

cd7 = ["Survivor", "Survivor", "Yesterday", "Survivor",]
cd8 = ["Survivor", "Waterfalls", "Survivor", "Faith",]
cd9 = ["Faith", "Survivor", "Survivor", "Survivor",]
cd_list3 = [cd7, cd8, cd9]

cd10 = ["Mamma mia", "Yesterday"]
cd11 = ["Mamma mia", "Yesterday"]
cd12 = ["Yesterday", "Mamma mia"]
cd13 = ["Yesterday", "Mamma mia"]
cd_list4 = [cd11, cd10]
cd_list5 = [cd10, cd12]
cd_list6 = [cd10, cd12, cd11, cd13]

cd14 = ["Thriller", "Thriller", "Lights", "Thriller"]
cd15 = ["Thriller", "Royals", "Vogue", "Closing"]
cd_list7 = [cd14, cd15]
