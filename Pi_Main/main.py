import serial
import time
import utils.bitmap_utils as bitmap_utils
import utils.pi_serial as pi_serial
import utils.referee as referee
import Pi_Main.game.chess_game as chess_game

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

                time.sleep(0.01)  # small delay to reduce CPU use

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("\nExited by user.")

if __name__ == "__main__":
    main()
