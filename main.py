from PIL import Image
import pyfiglet

from color import Red, Green, Blue, Yellow, Purple, Cyan, Style


ASCII_CHARS = "@%#*+=-:. "

COLORS = {
    "1": Red.RED4,
    "2": Green.GREEN4,
    "3": Blue.BLUE4,
    "4": Yellow.YELLOW4,
    "5": Purple.PURPLE4,
    "6": Cyan.CYAN4,
}



def clear():
    print("\033[2J\033[H", end="")


def pause():
    input("\nPress Enter to continue...")


def choose_color():
    print()
    print(f"{Style.BOLD}Choose a color:{Style.RESET}")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("4. Yellow")
    print("5. Purple")
    print("6. Cyan")

    while True:
        choice = input("\nColor [1]: ").strip() or "1"

        if choice in COLORS:
            return COLORS[choice]

        print(
            f"{Red.RED2}Invalid color. Choose 1-6."
            f"{Style.RESET}"
        )


def image_to_ascii(path, width=80):
    try:
        image = Image.open(path)

    except Exception as e:
        print(
            f"{Red.RED2}"
            f"Could not open image: {e}"
            f"{Style.RESET}"
        )
        return None

    # Convert image to grayscale
    image = image.convert("L")

    if image.width == 0:
        return None

    # Characters are usually taller than they are wide
    aspect_ratio = image.height / image.width

    height = max(
        1,
        int(width * aspect_ratio * 0.5)
    )

    image = image.resize(
        (width, height)
    )

    pixels = list(image.getdata())

    result = []

    for y in range(height):
        line = ""

        for x in range(width):
            pixel = pixels[
                y * width + x
            ]

            index = (
                pixel *
                (len(ASCII_CHARS) - 1)
                // 255
            )

            line += ASCII_CHARS[index]

        result.append(line)

    return "\n".join(result)


def picture_mode():
    clear()

    print(
        f"{Cyan.CYAN3}"
        f"=== PICTURE TO ASCII ==="
        f"{Style.RESET}\n"
    )

    path = input("Image path: ").strip()

    if not path:
        print(
            f"{Red.RED2}"
            "No image path entered."
            f"{Style.RESET}"
        )
        pause()
        return

    # Width
    while True:
        width_input = input("Width [80]: ").strip()

        if not width_input:
            width = 80
            break

        try:
            width = int(width_input)

            if width <= 0:
                raise ValueError

            break

        except ValueError:
            print(
                f"{Red.RED2}"
                "Width must be a positive number."
                f"{Style.RESET}"
            )

    ascii_art = image_to_ascii(
        path,
        width
    )

    if ascii_art is None:
        pause()
        return

    color = choose_color()

    clear()

    print(
        color +
        ascii_art +
        Style.RESET
    )

    # Save
    save = input(
        "\nSave to file? [y/N]: "
    ).strip().lower()

    if save == "y":
        filename = (
            input(
                "Filename [ascii.txt]: "
            ).strip()
            or "ascii.txt"
        )

        try:
            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:
                file.write(ascii_art)

            print(
                f"{Green.GREEN3}"
                f"Saved as {filename}"
                f"{Style.RESET}"
            )

        except Exception as e:
            print(
                f"{Red.RED2}"
                f"Could not save file: {e}"
                f"{Style.RESET}"
            )

    pause()


def get_fonts():
    """
    Returns all fonts installed
    with the current PyFiglet installation.
    """

    try:
        fonts = pyfiglet.FigletFont.getFonts()

        return sorted(fonts)

    except Exception:
        return ["standard"]


def choose_font():
    fonts = get_fonts()

    # Put standard first
    if "standard" in fonts:
        fonts.remove("standard")
        fonts.insert(0, "standard")

    print(
        f"{Cyan.CYAN3}"
        f"\nAvailable fonts:"
        f"{Style.RESET}\n"
    )

    # Show fonts in columns
    for i, font in enumerate(fonts, 1):
        print(f"{i:3}. {font}")

    print()

    while True:
        choice = input(
            f"Font number [1-{len(fonts)}]: "
        ).strip()

        # Default
        if not choice:
            return fonts[0]

        try:
            number = int(choice)

            if 1 <= number <= len(fonts):
                return fonts[number - 1]

        except ValueError:
            pass

        print(
            f"{Red.RED2}"
            f"Invalid font number."
            f"{Style.RESET}"
        )


def text_mode():
    clear()

    print(
        f"{Cyan.CYAN3}"
        f"=== TEXT TO ASCII ==="
        f"{Style.RESET}\n"
    )

    text = input("Enter text: ")

    if not text:
        print(
            f"{Red.RED2}"
            "No text entered."
            f"{Style.RESET}"
        )
        pause()
        return

    # Choose actual installed font
    font = choose_font()

    try:
        ascii_text = pyfiglet.figlet_format(
            text,
            font=font
        )

    except Exception as e:
        print(
            f"{Red.RED2}"
            f"Could not generate ASCII text: {e}"
            f"{Style.RESET}"
        )

        pause()
        return

    color = choose_color()

    clear()

    print(
        color +
        ascii_text +
        Style.RESET
    )

    # Save
    save = input(
        "\nSave to file? [y/N]: "
    ).strip().lower()

    if save == "y":
        filename = (
            input(
                "Filename [text_ascii.txt]: "
            ).strip()
            or "text_ascii.txt"
        )

        try:
            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:
                file.write(ascii_text)

            print(
                f"{Green.GREEN3}"
                f"Saved as {filename}"
                f"{Style.RESET}"
            )

        except Exception as e:
            print(
                f"{Red.RED2}"
                f"Could not save file: {e}"
                f"{Style.RESET}"
            )

    pause()



def main():
    while True:
        clear()

        title = pyfiglet.figlet_format(
            "ASCII ART",
            font="slant"
        )

        print(
            Cyan.CYAN3 +
            title +
            Style.RESET
        )

        print(
            f"{Style.BOLD}"
            "1. Picture -> ASCII"
            f"{Style.RESET}"
        )

        print(
            f"{Style.BOLD}"
            "2. Text -> ASCII"
            f"{Style.RESET}"
        )

        print(
            f"{Style.BOLD}"
            "3. Exit"
            f"{Style.RESET}"
        )

        choice = input(
            "\nSelect: "
        ).strip()

        if choice == "1":
            picture_mode()

        elif choice == "2":
            text_mode()

        elif choice == "3":
            clear()

            print(
                Green.GREEN3 +
                "Goodbye!" +
                Style.RESET
            )

            break

        else:
            print(
                f"{Red.RED3}"
                "Invalid option."
                f"{Style.RESET}"
            )

            pause()


if __name__ == "__main__":
    main()
