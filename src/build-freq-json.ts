const fs = require('fs');
const path = require('path');
const { parse } = require('fast-csv');

const readCsvAndWrite = async (csvFile: string, outputJson: string) => {
    const rows = await new Promise((r,j) => {
      let rows: {word: string; frq: number}[] = [];
      fs.createReadStream(csvFile)
        .pipe(parse({ headers: true }))
        .on('error', (error: any) => console.error(error))
        .on('data', (row: any) => {
            // console.log(row);
            //each row can be written to db
            rows.push({word: row['word'], frq: parseInt(row['frq'])});
        })
        .on('end', (rowCount:number) => {
            console.log(`Parsed ${rowCount} rows`);
            r(rows);
        });
    });
    fs.writeFileSync(outputJson, JSON.stringify(rows));
    console.log('output the json done ' + outputJson)
}
readCsvAndWrite('./ecdict.csv', './ecdict-frq.json');