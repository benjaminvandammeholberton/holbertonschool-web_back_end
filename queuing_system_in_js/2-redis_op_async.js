import { createClient } from "redis";
import redis from "redis";
import { promisify } from "util";

const client = createClient()
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: `, err)
  )
  .on("connect", () => console.log("Redis client connected to the server"));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const value = await get(schoolName);
  console.log(value);
}

async function main() {
  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");
}

main();
