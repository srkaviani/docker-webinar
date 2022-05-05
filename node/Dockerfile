FROM node:12
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
