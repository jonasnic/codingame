# Convert a message to binary
def toBinary(msg)
  binaryMsg = ""
  binary = ""

  # Loop trough the entire string to convert each character
  msg.each_char do |c|
    # Convert each character to a binary string
    binary = c.ord.to_s(2)
    # Add missing zeros to each binary string,
    # then add a new entry in the bin msg
    binaryMsg += binary.rjust(7, '0')
  end

  binaryMsg
end

# Convert a binary  message to unary
# noinspection RubyLocalVariableNamingConvention
def toUnary(msg)
  unaryMsg = ""
  digit = false
  count = 0

  # Loop trough the entire string to convert each character
  msg.each_char do |c|
    if count == 0 # New sequence of zeros
      if c == '0'
        digit = false # false = 0, true = 1
        unaryMsg += "00 0"
      else # New sequence of 1s
        digit = true
        unaryMsg += "0 0"
      end
      count += 1
    else # (count >= 1)
      if (c == '0') && digit # Switch from 1 to 0
        digit = false
        count = 1 # Reset the count
        unaryMsg += " 00 0"
      elsif (c == '1') && !digit # Switch from 0 to 1
        digit = true
        count = 1 # Reset the count
        unaryMsg += " 0 0"
      else # Repeated 0 or 1
        unaryMsg += "0"
        count += 1
      end
    end
  end

  unaryMsg
end

@message = gets.chomp

# Write an action using puts
# To debug: STDERR.puts "Debug messages..."
binaryMsg = toBinary(@message)
unaryMsg = toUnary(binaryMsg)
puts unaryMsg