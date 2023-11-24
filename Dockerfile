# docker run -d -p 5173:5173 -e VITE_HOST=0.0.0.0
FROM node:14

WORKDIR /app

COPY . .

RUN npm i 
RUN npm install react-router-dom
RUN npm install @mui/material
RUN npm install @emotion/react @emotion/styled
RUN npm install axios

EXPOSE 5173

CMD ["npm", "run", "dev"]