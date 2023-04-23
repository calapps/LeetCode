# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals, newInterval):
        
        # assuming that its not in place we can do it in O(n)
        # not in place, and its sorted by start[i] and we want ot retur
        # it in the same sorted order but with neWInterval inserted and possibly
        # merged if necessary
        
        # explanation of this code:
        # so we basically want to either append a num or merge it onto the thing
        # I suck at intervals btw but...
        # So we have 3 cases: 1) if our new interval doens't overlap with the current
        # interval and is before that interval
        # 2) if that new interval 

        res = []

        for i in range(len(intervals)):
            # newInt before int, then append the new interval and everything after
            # it
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # newInt is after int, then append the current int because the newInt
            # might overlap with the next int
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # if it does overlap, then we need to merge it 
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])]
        # have to append because of the case if we overtake everything
        res.append(newInterval)
        return res 
            
        
        # input = [1,2], [4,7], [12,18], [19,27]
        # new = [5,18] => [4,18] => [4,18]

        # res = [1,2] [4, 18], []




        # given an interval we want to insert into the list of intervals. We want
        # to append it to the intervals list and then merge it if necessary.
        # So there are two options: we either merge it (theres a variety of ways) or 
        # we just drop it in 
        # It is also already sorted in ascending order from start(i), so this 
        # means that that we could do it in O(n) because it's already sorted.
        # 
        # so the first way I would go about it would be to first insert it into 
        # the list and then try to merge it if necessary 
        # we need to do o(n) operations 
        # since we want to do it inplace, then this is our option
        # we can either obliterate and re-make the intervals or just modify it 
        # in place

        # intervals = [1,3],[5,7], int = [4,6]
        # iterate through intervals and check is int[0] > intervals[i][1], then
        # go to the next item, else if opposite is true, then check for every single
        # interval after [1,3] that if int[1] >= intervals[j][0] and subsequently
        # [j][1] then we can remove that OR we can modify it 
        # merge one by one 

        # the problem here is that we cannot go back in a sense,
        # but have to keep on moving forward because we are iterating
        # and our only option is to do list manipulations which idk which to do
        # in O(n) time.
        #
        # for num in intervals:
        #   if newint[0] > num[1]: continue
        #   else:
        #       for newerNums in intervals:
        #           if num[1] > 
        # if we do it in O(nlogn) time, then we would append it, then sort it again
        # then we would see if we need to merge by doing: (leverage the fact that)
        # they are not overlapping and also append an extra None to the end
        # 
        # for i in range(len(intervals)):
        #    if next is not none and intervals[i][1] < newint[0]: continue 
        #    else: merge by making intervalis[i][1] = newint[1], and then check If
        #    that newint is < next[0] < next[1], etc. and remove for every time
        #    and skip until we find one where it is > next[0] but also < next[1] and
        #    then set our intervalis[i] like we are consuming forward. lets try It
        #    in o(n) thoguh 
        #   YOU ASSUMED IT WAS INPLACE BECAUSE IT SAYS INSERT, IDK Those
        # ignore above and now assume that it doesn't have to be in place



        # ~~~~~~~~~~~
        
        # if newInt[1] < int[i]: append(newInt) append the rest
        # if newInt[0] > int[i]: appent int and loop
        # if newInt can be merged with int[i]: we don't append anything but just set
        # newInt to be the min and max of itself and the current num
        # if we add newInt then we return in the first if but if we never hit that
        # then we never add newInt therefore we add newInt to the end
        # We do iteration which is like recursion, but we are mutating 
        # newInt in real time so we can just leave it up to these three cases instead of thinking
        # of something convoluted and verbose