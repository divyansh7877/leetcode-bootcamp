class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        '''
        Problem Link: https://leetcode.com/problems/video-stitching/description/
        Solved by sorting and use two pointers.
        '''
        clips.sort()
        clips.append((time,time))
        max_end=-1
        pivot_start=0
        cnt=0

        i=0
        while i<len(clips):
            start,end=clips[i]

            if start<=pivot_start:
                max_end=max(max_end,end)
                i+=1

            else:
                pivot_start=max_end
                cnt+=1
                if max_end>=time:
                    return cnt

                elif start>max_end:
                    return -1


