choices = ["The Little Prince","The Hobbit","Harry Potter and the Philosopher's Stone","Dream of the Red Chamber","And Then There Were None","A Tale of Two Cities","The Lion, the Witch and the Wardrobe","She: A History of Adventure","Vardi Wala Gunda","The Da Vinci Code","Harry Potter and the Chamber of Secrets","Harry Potter and the Prisoner of Azkaban","Harry Potter and the Goblet of Fire","Harry Potter and the Order of the Phoenix","Harry Potter and the Half-Blood Prince","Harry Potter and the Deathly Hallows","The Alchemist ","The Catcher in the Rye","The Bridges of Madison County","Ben-Hur: A Tale of the Christ","You Can Heal Your Life","One Hundred Years of Solitude","Lolita","Heidi","The Common Sense Book of Baby and Child Care","Anne of Green Gables","Black Beauty","The Name of the Rose","The Eagle Has Landed","Watership Down","The Hite Report","Charlotte's Web","The Ginger Man","The Tale of Peter Rabbit","Jonathan Livingston Seagull","The Very Hungry Caterpillar","A Message to Garcia","To Kill a Mockingbird","Flowers in the Attic","Cosmos","Sophie's World","Angels & Demons","Kane and Abel","How the Steel Was Tempered","War and Peace","The Adventures of Pinocchio","The Diary of Anne Frank","Your Erroneous Zones","The Thorn Birds","The Purpose Driven Life","The Kite Runner","Valley of the Dolls","Alcoholics Anonymous Big Book","How to Win Friends and Influence People","The Great Gatsby","Gone with the Wind","Rebecca","Nineteen Eighty-Four","The Revolt of Mamie Stover","The Girl with the Dragon Tattoo","The Lost Symbol","The Hunger Games","James and the Giant Peach","The Young Guard","Who Moved My Cheese?","A Brief History of Time","Paul et Virginie","Lust for Life","The Wind in the Willows","The 7 Habits of Highly Effective People","Virgin Soil Upturned","The Celestine Prophecy","The Fault in Our Stars","The Girl on the Train","The Shack","Uncle Styopa","The Godfather","Love Story","Catching Fire","Mockingjay","Kitchen","Andromeda Nebula","Autobiography of a Yogi","Gone Girl","All Quiet on the Western Front","The Bermuda Triangle","Things Fall Apart","Animal Farm","Wolf Totem","The Happy Hooker: My Own Story","Jaws","Love You Forever","The Women's Room","What to Expect When You're Expecting","Adventures of Huckleberry Finn","The Secret Diary of Adrian Mole, Aged 13¾","Pride and Prejudice","Kon-Tiki: Across the Pacific in a Raft","The Good Soldier Švejk","Where the Wild Things Are","The Power of Positive Thinking","The Secret","Fear of Flying","Dune","Charlie and the Chocolate Factory","The Naked Ape","","Totto-chan, the Little Girl at the Window","Matilda","The Book Thief","The Horse Whisperer","Goodnight Moon","The Neverending Story","All the Light We Cannot See","Fifty Shades of Grey","Where the Crawdads Sing","The Outsiders","Guess How Much I Love You","Shōgun","The Poky Little Puppy","The Pillars of the Earth","Perfume","The Grapes of Wrath","The Shadow of the Wind","Interpreter of Maladies","Becoming","The Hitchhiker's Guide to the Galaxy","Tuesdays with Morrie","God's Little Acre","Follow Your Heart","A Wrinkle in Time","Long Walk to Freedom","The Old Man and the Sea","Life After Life","Me Before You","Norwegian Wood","Peyton Place","The Plague","No Longer Human","Man's Search for Meaning","The Divine Comedy","The Prophet","The Boy in the Striped Pyjamas","The Exorcist","The Gruffalo","Fifty Shades Darker","Ronia, the Robber's Daughter","The Cat in the Hat","Diana: Her True Story","The Help","Catch-22","The Stranger","Eye of the Needle","The Lovely Bones","Wild Swans","Santa Evita","Night","Confucius from the Heart","The Total Woman","Knowledge-value Revolution","Problems in China's Socialist Economy","What Color Is Your Parachute?","The Dukan Diet","The Joy of Sex","The Gospel According to Peanuts","The Subtle Art of Not Giving a Fuck","Life of Pi","The Giver","The Front Runner","The Goal","Fahrenheit 451","Angela's Ashes","The Story of My Experiments with Truth","Bridget Jones's Diary"]
# List of books taken from https://en.wikipedia.org/wiki/List_of_best-selling_books
IMAGES = ["""⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣆⢳⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣾⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⣄⠀⢠⣿⣿⣿⣿⡎⢻⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⢸⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣾⣿⣿⣿⣿⠃⠀⢸⣿⣿⣿⣿⣿⣿⠀⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⠏⠀⠀⣸⣿⣿⣿⣿⣿⡿⢀⣿⡆⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⡄
⠀⢰⠀⠀⣴⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⢠⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⣧
⠀⣿⡀⢸⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⣸⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣿⣷⣼⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⢹⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡄⢻⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⠇
⢳⣌⢿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⠏⠀
⠀⢿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠋⣠⠀
⠀⠈⢻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣵⣿⠃⠀
⠀⠀⠀⠙⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣦⣀⠀⠀⠀⠀⢀⣴⠿⠛⠁⠀⠀""", """+--------------^v^^
|           ^vvvv^^
|   BOOKS  vv^^^^v^
|      vvvvv^^>^vv^
|   vvvv^^^^^>^vvvv
|vvvvvv^^^^vv^vvvvv
vvvv^^vv<>^vvvvvvvv
vvvvvvvvv^>vvvvv v^
^^^^^>^ vvvvv^vv^^^
^^^<> ^^vvvvvvv^vvv
^^^^^^^vvvvv^^^v^vv
^^^ ^>vvv^^^^vvvvvv
^^^vvvvvvvv^vv^^^vv
^^vv^v^ vv^^^^^^vvv
^^vvvvvv<-^vvv^vvvv""", """+----------------^^
|              ^^^^
|   BOOKS    ^^^^v^
|          ^^^^^vv^
|        ^^^^^^vv^v
|      ^^^^^^^^v^^v
|     ^^^^^^^vvv^vv
|    ^^^^^ vvv^^ v^
|   ^^^ ^^vv^^vv^^^
|  ^^ ^^^vvvvvv^vvv
| ^^^^^vvvvv^^^v^vv
|^^ ^vvvv^^^^vvvvvv
^^^vvvvvvvv^vv^^^vv
^^vv^v^ vv^^^^^^vvv
^^vvvvvv<-^vvv^vvvv""", """+-----------------^
|                ^^
|   BOOKS       ^^^
|              ^^^^
|             ^^^^^
|            ^^^^^+
|           ^^^^^ ^
|          ^^^^^ ^^
|         ^^^^^^^^^
|        ^^^^^^^vvv
|      ^^^^ ^^^vvvv
|    ^^^^^^^^vvvvvv
|   ^^^^^vvvvv^^vvv
| ^^^^^ vv ^^^^^vvv
+-^^^^vvv+^vvvvvvvv""", """+-----------------+
|                 |
|   BOOKS         |
|                 |
|                 |
|                 |
|                 ^
|                ^^
|               ^^^
|              ^^^^
|             ^^^^^
|            ^^^^^v
|           ^^^^vvv
|          ^^^^^vvv
+---------^vvvvvvvv""", """+-----------------+
|                 |
|   BOOKS         |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                ^^
|               ^^^
+--------------^^^^""", """+-----------------+
|                 |
|   BOOKS         |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
+-----------------+"""]

# List of books taken from https://en.wikipedia.org/wiki/List_of_best-selling_books