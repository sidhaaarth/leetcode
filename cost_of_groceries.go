// Cost of Groceries
// Problem : https://www.codechef.com/practice/course/arrays/ARRAYS/problems/KITCHENCOST

package main
import (
    "fmt"
    "bufio"
    "strings"
    "os"
    "strconv"
    )
    
    
func PurchaseAllEqualToX( N int, freshnessIndex int, freshnessArr [] int, costArr [] int) int {
    total := 0
    for i:=0; i<N; i++{
        if freshnessArr[i]>=freshnessIndex {
            total += costArr[i]
        }
    }
    return total
}
func main(){
    reader := bufio.NewReader(os.Stdin)
    
    line, _ := reader.ReadString('\n')
    line = strings.TrimSpace(line)
    T,_ := strconv.Atoi(line)
    
    for i:=0; i<T; i++ {
        line, _ := reader.ReadString('\n')
        line = strings.TrimSpace(line)
        parts := strings.Fields(line)
        
        N, _ := strconv.Atoi(parts[0])
        freshnessIndex, _ := strconv.Atoi(parts[1])
        
        freshnessArr := make([]int, N)
        arr,_ := reader.ReadString('\n')
        arr = strings.TrimSpace(arr)
        arrStripped := strings.Fields(arr)
        for i,part := range arrStripped {
            freshnessArr[i],_ = strconv.Atoi(part)
        }
        
        costArr := make([]int, N)
        c_arr,_ := reader.ReadString('\n')
        c_arr = strings.TrimSpace(c_arr)
        c_arrStripped := strings.Fields(c_arr)
        for i,part := range c_arrStripped {
            costArr[i],_ = strconv.Atoi(part)
        }
        
        res := PurchaseAllEqualToX(N, freshnessIndex, freshnessArr, costArr)
        fmt.Println(res)
    }
}
