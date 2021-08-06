
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="the source image")
    parser.add_argument("dest", help="the dest text")

    if(len(sys.argv) < 3):
        parser.print_help()
    else:
        try:
            import cv2

            args = parser.parse_args()
            img = cv2.imread(args.src, 2)
            
            # THRESH_BINARY_INV (black = 1 , white = 0)
            # THRESH_BINARY (white = 1, black = 0)
            
            _, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
            
            binary = [[1 if pixel == 255 else pixel for pixel in row]
                      for row in bw_img]
            
            leng = len(binary)
            
            with open(args.dest, 'w') as dest:
                for r in range(0, leng - 1):
                    dest.write(''.join(map(str, binary[r])))
                    dest.write('\n')
            
                # dest.write('\n')
                # Original printing statement
                # dest.write(str(binary[-1]))

                # Remove square bracket printing statement
                # dest.write(str(binary[-1]).strip('[]'))

                # Remove square bracket printing statement and remove , and space
                dest.write(''.join(map(str, binary[-1])))
                dest.write('\n')
        except:
            print('If you don’t have OpenCV installed, install it via pip.')
            print('> pip install opencv-python')


main()
