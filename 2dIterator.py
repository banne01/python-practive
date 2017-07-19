'''

Airbnb: 2D Iterator with remove() 

Implement a 2D iterator, with method next(), hasNext() and remove().


 Understand the problem:
The question is close to the Leetcode Flatten 2D iterator. The only thing needs to take care is the remove() method. 

 According to the definition of the remove(), 
Removes from the underlying collection the last element returned by this iterator (optional operation). This method can be called only once per call to next(). The behavior of an iterator is unspecified if the underlying collection is modified while the iteration is in progress in any way other than by calling this method.

 So the remove() method actually removes the element returned from the next(). 

To safely remove from a collection while iterating over it you should use an Iterator.

For example:
List<String> names = ....
Iterator<String> i = names.iterator();
while (i.hasNext()) {
   String s = i.next(); // must be called before you can call i.remove()
   // Do something
   i.remove();
}

How exactly Iterator removes elements depends on its implementation, which may be different for different Collections. Definitely it doesn't break the loop you're in. I've just looked how ArrayList iterator is implemented and here's the code:
public void remove() {
    if (lastRet < 0)
        throw new IllegalStateException();
    checkForComodification();

    try {
        ArrayList.this.remove(lastRet);
        cursor = lastRet;
        lastRet = -1;
        expectedModCount = modCount;
    } catch (IndexOutOfBoundsException ex) {
        throw new ConcurrentModificationException();
    }
}

Code (Java):
import java.io.*;
import java.util.*;

public class Solution {
  private List<List<Integer>> array;
  private int rowId;
  private int colId;
  private int numRows;
  
  public Solution(List<List<Integer>> array) {
    this.array = array;
    rowId = 0;
    colId = 0;
    numRows = array.size();
  }
  
  public boolean hasNext() {
    if (array == null || array.isEmpty()) {
      return false;
    }
    
    while (rowId < numRows && (array.get(rowId) == null || 
      array.get(rowId).isEmpty())) {
      rowId++;
    }
    
    return rowId < numRows;
  }
  
  public int next() {
    int ret = array.get(rowId).get(colId);
    colId++;
    if (colId == array.get(rowId).size()) {
      rowId++;
      colId = 0;
    }
    
    return ret;
  }
  
  public void remove() {
    List<Integer> listToRemove;
    int rowToRemove;
    int colToRemove;
    
    // Case 1: if the element to remove is the last element of the row
    if (colId == 0) {
      rowToRemove = rowId - 1;
      listToRemove = array.get(rowToRemove);
      colToRemove = listToRemove.size() - 1;
      
      listToRemove.remove(colToRemove);
    } else { // Case 2: the element to remove is not the last element
      rowToRemove = rowId;
      listToRemove = array.get(rowToRemove);
      colToRemove = colId - 1;
      listToRemove.remove(colToRemove);
    }
    
    // If the list to remove has only one element
    if (listToRemove.isEmpty()) {
      array.remove(listToRemove);
      rowId--;
    }
    
    // Update the colId
    if (colId != 0) {
      colId--;
    }
  }
  
  public static void main(String[] args) {
    List<List<Integer>> array = new ArrayList<>();
    List<Integer> row1 = new ArrayList<>();
    row1.add(1);
    row1.add(2);
    row1.add(3);
    
    array.add(row1);
    
    List<Integer> row3 = new ArrayList<>();
    array.add(row3);
    
    List<Integer> row2 = new ArrayList<>();
    row2.add(4);
    row2.add(5);
    array.add(row2);
    
    Solution sol = new Solution(array);
    while (sol.hasNext()) {
      int result = sol.next();
      System.out.println(result);
      
      if (result == 3) {
        sol.remove();
      }
    }
    
    System.out.println();
    
    for (List<Integer> row : array) {
      for (Integer elem : row) {
        System.out.println(elem);
      } 
    }
  }
  
}

'''
