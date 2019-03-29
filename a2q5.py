# = = = = = = = = = = = = = = = = = =
#Question 5 [ Data Hiding]
#Student Name: Adrian Lim Song En
#Student Number: s3710625
# = = = = = = = = = = = = = = = = = =
from PIL import Image

#Function to only accept 7 numbers
def user_input():
    checker = False
    id_length = 7
    while checker is False:
        user_input = input('Enter your student number: ')
        if  len(user_input) is id_length:
            try:
                id = int(user_input)
                checker = True
            except ValueError:
                print("Enter only your number")
        else:
            print('Invalid student ID')
            checker = False
    binary_id = int(int_to_bin(id))
    return binary_id

#Function to convert integers to binary
def int_to_bin(int):
    binary = bin(int).split('b')[1]
    return binary

#Function to convert binary to integers
def bin_to_int(bin):
    integer = int(bin, 2)
    return integer

#Function to get the RGB value of a desired pixel from a given image
def get_pixel(image, x, y):
    # Inside image bounds?
    width, height = image.size
    if x >= width or y >= height:
      return None

    # Get Pixel
    rgb_image = image.convert('RGB')
    r, g, b = rgb_image.getpixel((x, y))
    return r, g, b

#Function to print all the pixels and their coordinates with their RGB values
def print_all_pixel(image):
    width, height = image.size
    row = 0
    column = 0
    rgb_value = ''

    rgb_image = image.convert('RGB')

    while column < height:
        while row < width:
            #Slow ( Neater )
            #rgb_value += "Pixel (R,G,B) -> " + str(rgb_image.getpixel((row, column)))
            #print('Row number    -> ' + str(row))
            #print('Column number -> ' + str(column))
            #print('Coordinates   -> [' + str(row) + ',' + str(column) + ']')
            #print(rgb_value)
            rgb_value = ''
            #print('')

            #Fast (Messy)
            rgb_value += " | Pixel [" + str(row) + "," + str(column) + "] -> " + str(rgb_image.getpixel((row, column)))
            row += 1
        print(rgb_value)
        rgb_value = ''
        column +=1
        row = 0

#Function to hide a part of the message in a desried pixel R(red) value given the image
def hiding_message(image, x, y, message_array, count):
    r, g, b = get_pixel(image, x, y)
    pixel_binary = int_to_bin(int(r))
    bin_array = list(pixel_binary)
    bin_array.pop()
    bin_array.append(message_array[count])
    modified_pixel = bin_to_int(str(''.join(bin_array)))
    modified_color = (modified_pixel, g, b)
    image.putpixel((x, y), modified_color)

#Function to extract the hidden message from a desired pixel R(red) value
def finding_message(image, x, y):
    r, g, b = get_pixel(image, x, y)
    pixel_binary = int_to_bin(int(r))
    bin_array = list(pixel_binary)
    message_part = bin_array[-1]
    return message_part

#Function for Mona Lisa steganography [ Encoding & Decodings]
def mona_lisa_steganography(secret_message):
    #Encoding message to picture
    print('Encoding student ID. . .')
    img = Image.open('mona_lisa.jpg')
    #print(get_pixel(img, 10, 50))
    number_to_hide = str(secret_message)
    secret_array = list(number_to_hide)
    try:
        count1 = 0
        count2 = 10
        count3 = 50
        while count1 < 22:
            hiding_message(img, count2, count3, secret_array, count1)
            count1 += 1
            count2 += 10
            count3 += 50
    except IndexError:
        print('Can not hide message')
        exit()
    img.save('Encoded_mona_lisa.png')

    print('          |')
    print('          v')
    print('. . .Please wait. . .')
    print('          |')
    print('          v')

    #Decoding message to picture
    print('Decoding student ID. . .')
    encoded_picture = Image.open('Encoded_mona_lisa.png')
    #print(get_pixel(encoded_picture, 10, 50))
    message_list = []
    count4 = 0
    count5 = 10
    count6 = 50
    while count4 < 22:
        message_list.append(finding_message(encoded_picture, count5, count6))
        count4 += 1
        count5 += 10
        count6 += 50
    decrypted_message = bin_to_int(str(''.join(message_list)))
    print('Decrpted data: ' + str(decrypted_message))

# = = = = = = = = = = = = = = = = = =

#img = Image.open('mona_lisa.jpg')
#print_all_pixel(img)

mona_lisa_steganography(user_input())
