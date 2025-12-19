import trackio
import random
import time


runs = 3
epochs = 8

for run in range(runs):
    trackio.init(
        project="my-project-2",
        config = {"learning_rate": 0.001, "epochs":epochs, "batch_size":64},
        name= "samray-{}".format(run),
        resume="must"
    )

    for epoch in range(epochs):
        train_loss = random.uniform(0.2, 1.0)
        val_loss = random.uniform(0.2, 1.0)

        trackio.log(
            {
            "epoch": epoch,
            "train_loss": train_loss,
            "val_loss": val_loss,
            "image": trackio.Image(value="./iphone.jpg", caption="Iphone")
            }
        )
        time.sleep(0.2)

trackio.finish()
    





