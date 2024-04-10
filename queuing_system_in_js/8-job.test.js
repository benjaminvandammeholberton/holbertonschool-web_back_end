import { expect } from "chai";
import { describe, before, afterEach, after } from "mocha";
import { createQueue } from "kue";
import createPushNotificationsJobs from "./8-job";
import { spy, assert } from "sinon";

describe("createPushNotificationsJobs", () => {
  const queue = createQueue();

  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it("should display a error message if jobs is not an array", () => {
    expect(() => createPushNotificationsJobs(1, queue)).to.throw(
      Error,
      "Jobs is not an array"
    );
  });

  it("should create two new jobs to the queue", () => {
    const mockArray = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
      },
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
      },
    ];
    createPushNotificationsJobs(mockArray, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it("the type of data should be 'push_notification_code_3'", () => {
    const mockArray = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
      },
    ];
    createPushNotificationsJobs(mockArray, queue);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
  });

  it("the content of data should be the same than the mockArray", () => {
    const mockArray = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
      },
    ];
    createPushNotificationsJobs(mockArray, queue);
    expect(queue.testMode.jobs[0].data).to.deep.equal({
      phoneNumber: "4153518780",
      message: "This is the code 1234 to verify your account",
    });
  });
});
