object May15 {                                                                                                        
  def main(args: Array[String]): Unit = {                                                                             
    // Print List Head and Tail element                                                                              
                                                                                                                     
    val alist: List[Int] = List(1,2,3,5)                                                                             
    val firstlist = alist.head                                                                                       
    val lastlist = alist.tail                                                                                        
    println(firstlist)                                                                                               
    println(alist.mkString( ", "))                                                                                   
    println(lastlist.mkString( ", "))                                                                                
                                                                                                                     
    // Print List of String Head and Tail element                                                                    
                                                                                                                     
    val aStringList = List("Hello","A","B")                                                                          
    val word = aStringList.head                                                                                      
    val word1 = aStringList.tail                                                                                     
    println(word)                                                                                                    
    println(word1.mkString(", "))                                                                                    
                                                                                                                     
    // Print Array Head and Tail element                                                                             
                                                                                                                     
    val aArray: Array[Int] = Array(10,20,30,40)                                                                      
    val aFirst = aArray.head                                                                                         
    val aSecond = aArray.tail                                                                                        
    println(aFirst)                                                                                                  
    println(aSecond.mkString(", "))                                                                                  
                                                                                                                     
    // Print Set Head and Tail element                                                                               
                                                                                                                     
    val aSet: Set[Int] = Set(11,22,33,44,22,11)                                                                      
    val setFirst = aSet.head                                                                                         
    println(setFirst)                                                                                                
    val setLast = aSet.tail                                                                                          
    println(setLast.mkString(", "))                                                                                  
                                                                                                                     
    //   Print Set Head and Tail element                                                                             
                                                                                                                     
    val myMap: Map[String,Int]  = Map("Lakshmi" -> 1, "Baran" -> 2)                                                  
    val headMap = myMap.head                                                                                         
    val tailMap = myMap.tail                                                                                         
    println(headMap.productIterator.mkString(","))                                                                   
    println(tailMap.mkString(", "))                                                                                  
    println(tailMap.map { case (k, v) => s"$k: $v" }.mkString(", "))                                                 
                                                                                                                     
        // Map Loop through                                                                                          
                                                                                                                     
     val myMap2:  Map[String, Int] = Map("Apple" -> 3, "Grape" -> 4, "Orange" -> 8, "Banana" -> 5)                   
     val headmyMap2 = myMap2.head                                                                                    
    val tailmyMap2 = myMap2.tail                                                                                     
    println(headmyMap2.productIterator.mkString(",") )                                                               
                                                                                                           
     tailmyMap2.foreach{case(k,v) => println(s"Key = $k ,Value = $v")   }                                            
                                                                                                                     
}
}
                                                                                                                     
  }                                                                                                                  
