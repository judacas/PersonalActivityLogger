FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm install

# Copy configuration files first
COPY vite.config.ts tsconfig.json tsconfig.node.json vitest.config.ts ./

# Copy public directory
COPY public ./public

# Copy src directory
COPY src ./src

# Copy index.html to root
COPY index.html ./

# Expose port
EXPOSE 3000

# Run dev server
CMD ["npm", "run", "dev"]

