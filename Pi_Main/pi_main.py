import serial
import time
import bitmap_utils
import pi_serial
import referee
import chess_game

def main():
    SERIAL_PORT = "/dev/cu.usbmodem101"
    BAUD_RATE = 9600

    game = chess_game.Game()

    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            time.sleep(2)  # Give Arduino time to reset
            print("Running...")

            while True:
                # Check serial
                bitmap = pi_serial.read_serial(ser)
                if bitmap is not None:
                    bitmap = bitmap_utils.bitmapLine_to_bitmap(bitmap)
                    print("New bitmap received:")
                    if referee.check_starting_position(bitmap):
                        game = chess_game.Game()
                        print(game.board)
                    else:
                        game.update_bitmap(bitmap)

                # Do other tasks here
                do_something_else()
                update_gui()
                run_logic()

                time.sleep(0.01)  # small delay to reduce CPU use

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("\nExited by user.")

def do_something_else():
    # Your logic here
    pass

def update_gui():
    # Your logic here
    pass

def run_logic():
    pass

if __name__ == "__main__":
    main()
