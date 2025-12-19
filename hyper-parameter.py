import trackio
import random
for batch_size in [8,16,32]:
    for lr in [1e-5, 2e-5, 5e5]:
        trackio.init(
            project = "personal-test",
            name = f"lr-{lr}-batch-size-{batch_size}",
            config = {
                "lr" : lr,
                "batch-size" : batch_size
            }
        )

        trackio.log({"accuracy" : random.uniform(0.2, 1.0)})

trackio.finish()
    
