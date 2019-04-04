import java.util.Scanner

const val BASE_INDENT = 4

class CGXFormatter {
  var insideString = false
  var totalIndent = 0
  var newLine = true

  fun readLines() {
    val input = Scanner(System.`in`)
    val n = input.nextInt()
    if (input.hasNextLine()) {
      input.nextLine()
    }
    for (i in 0 until n) {
      val line = input.nextLine()
      for (char in line) {
        readChar(char)
      }
    }
  }

  fun readChar(char: Char) {
    if (insideString) {
      if (char == '\'') {
        insideString = false
      }
      printChar(char)
    } else {
      readCharOutsideString(char)
    }
  }

  fun readCharOutsideString(char: Char) {
    if (char == ' ' || char == '\t') {
      return
    }
    when (char) {
      '\'' -> {
        insideString = true
        printChar(char)
      }
      '(' -> {
        if (!newLine) {
          printNewLine()
        }
        printChar(char)
        printNewLine()
        totalIndent += BASE_INDENT
      }
      ')' -> {
        totalIndent -= BASE_INDENT
        if (!newLine) {
          printNewLine()
        }
        printChar(char)
      }
      ';' -> {
        printChar(char)
        printNewLine()
      }
      else -> printChar(char)
    }
  }

  fun printChar(char: Char) {
    if (newLine) {
      for (i in 0 until totalIndent) {
        print(' ')
      }
      newLine = false
    }
    print(char)
  }

  fun printNewLine() {
    println()
    newLine = true
  }
}

fun main(args : Array<String>) {
  val formatter = CGXFormatter()
  formatter.readLines()
}
