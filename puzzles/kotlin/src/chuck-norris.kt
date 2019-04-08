import java.util.Scanner

fun main(args : Array<String>) {
  val input = Scanner(System.`in`)
  val message = input.nextLine()
  val binary = toBinary(message)
  var unary = toUnary(binary)
  println(unary)
}

fun toBinary(text: String): String {
  var binary = StringBuilder()
  for (char in text) {
    val binaryStr = Integer.toBinaryString(char.toInt())
    val number = binaryStr.toInt()
    binary.append(String.format("%07d", number))
  }
  return binary.toString()
}

fun toUnary(text: String): String {
  val unary = StringBuilder()
  var prevDigit = false // false = 0, true = 1
  if (text.isNotEmpty()) {
    val char = text[0]
    if (char == '0') {
      unary.append("00 0")
    } else {
      unary.append("0 0")
      prevDigit = true
    }
  }

  (1 until text.length)
      .asSequence()
      .map { text[it] }
      .forEach {
        if (it == '0' && prevDigit) {
          unary.append(" 00 0") // switch from 1 to 0
          prevDigit = false
        } else if (it == '1' && !prevDigit) {
          unary.append(" 0 0") // switch from 0 to 1
          prevDigit = true
        } else {
          unary.append("0") // repeat digit
        }
      }

  return unary.toString()
}
