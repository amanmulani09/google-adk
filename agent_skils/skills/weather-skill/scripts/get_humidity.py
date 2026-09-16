import argparse

def get_humidity(location:str) -> str:
    """
    fetch live humidity for given location.
    """

    print(f"fetching live humidity for {location}")
    
    return "45%"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--location", type=str,default="Pune")
    args = parser.parse_args()
    
    print(get_humidity(args.location))

