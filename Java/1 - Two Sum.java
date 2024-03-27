class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hm = new HashMap<Integer,Integer>();
        for(int i = 0; i < nums.length; i++) {
            int required = target - nums[i]; 
            if(hm.containsKey(required)) {
                int[] arr = {hm.get(required), i};
                return arr; 
            }
            hm.put(nums[i], i);
        }
        return null;
    }
}
