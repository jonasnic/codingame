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
      for (character in line) {
        readChar(character)
      }
    }
  }

  fun readChar(character: Char) {
    if (insideString) {
      if (character == '\'') {
        insideString = false
      }
      printChar(character)
    } else {
      readCharOutsideString(character)
    }
  }

  fun readCharOutsideString(character: Char) {
    if (character == ' ' || character == '\t') {
      return
    }
    when (character) {
      '\'' -> {
        insideString = true
        printChar(character)
      }
      '(' -> {
        if (!newLine) {
          printNewLine()
        }
        printChar(character)
        printNewLine()
        totalIndent += BASE_INDENT
      }
      ')' -> {
        totalIndent -= BASE_INDENT
        if (!newLine) {
          printNewLine()
        }
        printChar(character)
      }
      ';' -> {
        printChar(character)
        printNewLine()
      }
      else -> printChar(character)
    }
  }

  fun printChar(character: Char) {
    if (newLine) {
      for (i in 0 until totalIndent) {
        print(' ')
      }
      newLine = false
    }
    print(character)
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
