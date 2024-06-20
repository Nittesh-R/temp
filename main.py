from fashion import filterLinks
from fashion_image import get_image

def main():
    final_link = filterLinks()
    get_image(final_link)

if __name__ == "__main__":
    main()
