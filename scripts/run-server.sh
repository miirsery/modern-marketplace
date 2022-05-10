npm install \
  --prefer-offline \
  --frozen-lockfile \
  --non-interactive \
  --production=false

npm build

rm -rf node_modules && \
  NODE_ENV=production npm install \
  --prefer-offline \
  --pure-lockfile \
  --non-interactive \
  --production=true

npm start