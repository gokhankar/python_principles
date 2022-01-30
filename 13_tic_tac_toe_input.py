"""
Tic tac toe input
Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, 
where the board looks like this:

1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C

The board is represented as a 2D list:

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
Imagine if your user enters "C1" and you need to see if there's an X or O 
in that cell on the board. To do so, you need to translate from the string 
"C1" to row 0 and column 2 so that you can check board[row][column].

Your task is to write a function that can translate from strings of length 2 
to a tuple (row, column). Name your function get_row_col; it should take a
 single parameter which is a string of length 2 consisting of an uppercase 
 letter and a digit.

For example, calling get_row_col("A3") should return the tuple (2, 0) because
 A3 corresponds to the row at index 2 and column at index 0in the board.

"""
"""
Bir tic-tac-toe (SOS) oyunu yazdığınızı hayal edin. Oyun tahtası aşağıdaki gibidir.

1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C

Oyun tahtasını iki boyutlu bir litse olarak olarak düşünelim, 

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

Kullanıcınızın "C1" girdiğini düşünün. Tahtadaki o hücrede X mi yoksa O mu olduğunu
görmeniz gerekiyor. Bunun için "C1" stringini satır 0 ve kolon 2 şeklinde çevirmelisiniz.
Ve board[satır][sütun] şeklinde(board[0][2]) yazabilirsiniz.

Şimdi göreviniz bir fonksiyon yazmak. Bu fonksiyon ("C1", "A2", "B0" vb. gibi) stringleri
iki elemanlı bir tuple (satır, sütun) haline getirmek olacak.

Fonksiyonunuzun ismi get_row-col olsun ve biri büyük harf diğeri rakamdan oluşan 
tek bir string parametre alsın.

Mesela, get_row_col("A3") fonskiyonu (2,0) şeklinde bir tuple dönmeli. Çünkü
A3 oyun tahtasında satır indexi 2 ye, sütun indexi ise 0 a karşılık geliyor.
"""
