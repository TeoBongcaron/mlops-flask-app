import argparse
import requests
import json

def main():
     parser = argparse.ArgumentParser(description='ML Ops CLI Tool')
     parser.add_argument('--weight', type=int, required=True, help='Weight of the MLB player in pounds')
     args = parser.parse_args()

     payload = {'weight': args.weight}
     response = requests.post(
         'https://ml-2319078f31e841f786ab97b8717011bf.ecs.us-east-1.on.aws/predict',
         json=payload
     )
     print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
     main()
