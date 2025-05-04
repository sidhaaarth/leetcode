// Take Discount or Not
// Problem : https://www.codechef.com/practice/course/arrays/ARRAYS/problems/DISCOUNTT?tab=statement


package main

import (
    "bufio"      // Efficient input
    "fmt"        // For printing
    "os"         // For standard input
    "strconv"    // Convert string to int
    "strings"    // Split input strings
)

func takeDiscountOrNot(X int, Y int, arr [] int) string {
    initalSum := 0
    
    for _,num := range arr {
        initalSum += num
    }
    differentialSum := 0
    for _,num := range arr{
        diff := num-Y
        // fmt.Println(diff, "diff")
        if diff < 0{
            diff = 0
        }
        differentialSum += diff
        // fmt.Println(differentialSum, "differentialSum")
    }
    
    totalCostWithCoupon := differentialSum + X
    // fmt.Println(totalCostWithCoupon, "totalCostWithCoupon")
    if totalCostWithCoupon < initalSum {
        return "COUPON"
    } else {
        return "NO COUPON"
    }
    
}

func main() {
    reader := bufio.NewReader(os.Stdin)
    
    line, _ := reader.ReadString('\n')
    line = strings.TrimSpace(line)
    T,_ := strconv.Atoi(line)
    
    for i:=0; i<T; i++ {
        line, _ := reader.ReadString('\n')
        line = strings.TrimSpace(line)
        parts := strings.Fields(line)
            
        // fmt.Println(parts, "parts")
        X,_ := strconv.Atoi(parts[1])
        Y,_ := strconv.Atoi(parts[2])
        
        arr, _ := reader.ReadString('\n')
        arr = strings.TrimSpace(arr)
        arrStripped := strings.Fields(arr)
        
        nums := make([]int, len(arrStripped))
        for i,part := range arrStripped {
            nums[i],_ = strconv.Atoi(part)
        }
        // fmt.Println(nums, "nums")
        res := takeDiscountOrNot(X, Y, nums)

        // 5️⃣ Print the result
        fmt.Println(res)
        
    }
}