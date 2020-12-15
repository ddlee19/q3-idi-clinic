cp ../data/uniquebrands.csv ./
cp ../data/brands.csv ./
cp ../data/brand_mills.csv ./
cp ../data/uniquemills.csv ./
docker build -t web-server .
docker run -p 5000:5000 web-server
