from pathlib import Path
from psij import Job, JobSpec, JobExecutor, ResourceSpecV1


def single_job(executor):
    """submit a single job and wait for it to complete.
    
    Args:
        executor: The JobExecutor instance to use.
    
    Returns:
        int: The exit code of the job.
    """
    output_file = "psij_local_date.txt"
    job = Job(
        JobSpec(
            executable='/bin/date', 
            stdout_path=Path(output_file)
        )
    )
    executor.submit(job)
    status = job.wait()
    exitcode = status.exit_code if status else None

    with open(output_file) as f:
        print(f.read())
    return exitcode


def multiple_jobs(executor):
    """submit multiple jobs and wait for them to complete.
    
    Args:
        executor: The JobExecutor instance to use.
    
    Returns:
        list: The exit codes of the jobs.
    """
    output_file_prefix = "psij_local_hello_"
    jobs = []
    for i in range(10):
        job = Job(
            JobSpec(
                executable='/bin/echo', 
                arguments=[f'Hello from job {i}'],
                stdout_path=Path(f"{output_file_prefix}{i}.txt")
            )
        )
        executor.submit(job)
        jobs.append(job)
    
    long_job = Job(JobSpec(executable='/bin/sleep', arguments=['60']))
    executor.submit(long_job)

    exitcodes = []
    for i in range(10):
        status = jobs[i].wait()
        exitcodes.append(status.exit_code if status else None)
        with open(f"{output_file_prefix}{i}.txt") as f:
            print(f.read())
    
    print(long_job.status.state)
    long_job.cancel()
    exitcodes.append(long_job.status.exit_code)
    
    return exitcodes

def mpi_job(executor):
    """submit a single MPI job and wait for it to complete.
    
    Args:
        executor: The JobExecutor instance to use.
    
    Returns:
        int: The exit code of the job.
    """
    output_file = Path("psij_local_mpi_hello.txt")
    mpi_job = Job(
        JobSpec(
            executable='hello', 
            stdout_path=output_file,
            resources=ResourceSpecV1(process_count=4),
            launcher='mpirun'
        )
    )

    executor.submit(mpi_job)
    status = mpi_job.wait()

    with open(output_file) as f:
        print(f.read())
    return status.exit_code if status else None
    

if __name__ == "__main__":
    executor = JobExecutor.get_instance('local')
    single_exit_code = single_job(executor)
    multiple_exit_codes = multiple_jobs(executor)
    mpi_exit_code = mpi_job(executor)

    print("Single job exit code: ", single_exit_code)
    print("Multiple jobs exit codes: ", multiple_exit_codes)
    print("MPI job exit code: ", mpi_exit_code)
