import kue from "kue";

const queue = kue.createQueue();

const jobData = {
  phoneNumber: "123456789",
  message: "Hello",
};

const job = queue
  .create("push_notification_code", jobData)
  .save(function (err) {
    if (!err) console.log("Notification job created:", job.id);
  })
  .on("complete", (result) => console.log("Notification job completed"))
  .on("failed", (error) => console.log("Notification job failed"));
