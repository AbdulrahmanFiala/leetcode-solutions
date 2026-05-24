class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> uniqueSet = new HashSet<>();
        for (int num: nums){
            if(uniqueSet.contains(num)){
                return true;
            }
            uniqueSet.add(num);
        }
        return false;
    }
}