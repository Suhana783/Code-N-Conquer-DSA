//1.Reverse a String
//Given a string, reverse it without using built-in reverse functions.

// word = "hello"
// reverse_word = ""

// for (let i = 0; i < word.length; i++) {
//     reverse_word = word[i] + reverse_word
// }

// console.log(reverse_word)


// # 2.Check Palindrome
// # Determine if a given string is a palindrome (reads the same forwards and backwards).

function palindromeChecker (word) {
    i = 0
    j = word.length-1

    while (i <= j && j < word.length) {

        if (word[i] === word[j]) {
            i ++
            j --
        }

        else {
            return "not a palindrome"
        }
  
    }
    return "is palindrome"  
}

word = "oarraq"
console.log(palindromeChecker(word))