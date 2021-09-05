#Runtime: 28 ms, faster than 97.84% of Python3 online submissions for Distribute Candies to People.
#Memory Usage: 14.3 MB, less than 51.48% of Python3 online submissions for Distribute Candies to People.

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        m = int((-1+(1+8*candies)**(0.5))//2)
        r = m%num_people
        times = (m-r)//num_people
        l = [((i+1)*times+num_people*times*(times-1)//2) for i in range(num_people)]
        for i in range(r):
            l[i] += num_people*times + i + 1
        l[r] += candies - sum(l)
        return l
