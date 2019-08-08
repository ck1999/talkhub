FROM node:10-alpine

ARG static_build=1
RUN apk add --no-cashe bash
WORKDIR /usr/src/app

COPY ./package*.json ./ 

RUN if [ $static_build = 1 ] ; then npm ci ; fi

COPY . .

RUN if [ $static_build = 1 ] ; then npm run build ; fi


ENV HOST=0.0.0.0 
ENV PORT=5000
EXPOSE 5000

CMD ["npm", "run", "start"]