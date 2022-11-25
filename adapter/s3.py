import os, io, gzip, boto3

from adapter.library.logger import CloudWatch

cloudwatch = CloudWatch('S3')

class S3 (S3_Output):

    @cloudwatch.debug
    def __init__(self, debug):
        """ constructs new 'S3' object.

            :param debug: set debug mode

            :return: none
        """
        super().__init__()

        self.debug = debug

        self.session = boto3.Session()
        self.resource = self.session.resource('s3')
        self.client = self.session.client('s3')

    @cloudwatch.debug
    def dataframe_to_s3(self, path, filename, df):
        """ convert dataframe and write to either disk or s3.

            :param path: path where file should be saved
            :param filename: name of file dataframe should be saved as
            :param df: dataframe to be saved

            :return: none
        """
        if self.debug: self.to_disk(path, filename, df)
        else: self.to_s3(path, filename, df)
        
class S3_Output:

    @cloudwatch.debug
    def to_s3(self, path, filename, df):
        """ convert dataframe to csv, then gzip and write to s3.
        """
        dbuffer = io.StringIO()
        df.to_csv(dbuffer, index=False)
        dbuffer.seek(0)
        
        gbuffer = io.BytesIO()
        with gzip.GzipFile(mode='w', fileobj=gbuffer) as gfile:
            gfile.write(bytes(dbuffer.getvalue(), 'utf-8'))

        self.resource.Object(self.bucket_name, f"{path}{filename}").put(Body=gbuffer.getvalue())

    @cloudwatch.debug
    def to_disk(self, path, filename, df):
        """ convert dataframe to csv and write to disk.
        """
        if not os.path.exists(f"debug/{path}"): os.makedirs(f"debug/{path}")
        df.to_csv(f"debug/{path}{filename}", index=False, compression=None)
