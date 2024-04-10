import express from "express";
import { createClient } from "redis";
import { promisify } from "util";

const listProducts = [
  {
    id: 1,
    name: "Suitcase 250",
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: "Suitcase 450",
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: "Suitcase 650",
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: "Suitcase 1050",
    price: 550,
    stock: 5,
  },
];

function getItemById(id) {
  return listProducts.find((obj) => obj.id === id);
}

const app = express();
const client = createClient();

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

const clientGet = promisify(client.get).bind(client);

async function getCurrentReservedStockById(itemId) {
  const stock = await clientGet(`item.${itemId}`);
  return stock;
}

app.get("/list_products", (req, res) => {
  const response = listProducts.map((obj) => ({
    itemId: obj.id,
    itemName: obj.name,
    price: obj.price,
    initialAvailableQuantity: obj.stock,
  }));
  res.json(response);
});

app.get("/list_products/:itemId", async (req, res) => {
  const currentReservedStock = await getCurrentReservedStockById(
    req.params.itemId
  );
  const item = getItemById(Number(req.params.itemId));
  if (!item) {
    res.json({ status: "Product not found" });
  }
  const response = {
    itemID: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: item.stock - Number(currentReservedStock),
  };

  res.json(response);
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const item = getItemById(Number(req.params.itemId));
  if (!item) {
    res.json({ status: "Product not found" });
  }

  const currentReservedStock = await getCurrentReservedStockById(
    req.params.itemId
  );

  const itemInStock = item.stock - Number(currentReservedStock);

  if (itemInStock == 0) {
    res.json({
      status: "Not enough stock available",
      itemId: req.params.itemId,
    });
  } else {
    reserveStockById(req.params.itemId, Number(currentReservedStock) + 1);
    res.json({ status: "Reservation confirmed", itemId: req.params.itemId });
  }
});

app.listen(1245);
