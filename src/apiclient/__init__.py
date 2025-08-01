import json
import os
import sys

from typing import List
from typing_extensions import Annotated

import httpx
import typer

from dotenv import load_dotenv
from httpx import HTTPStatusError, RequestError
from loguru import logger

from apiclient.api_types import (
    HarmonizationRequest,
    HarmonizationResponse,
    HarmonizationVariation,
    
    HarmonizationTable,
    RecommendRequest,
    RecommendSchema
)

HARMONIZATION_DEFAULT_API_URL = "https://apiserver.netriasbdf.cloud/v1/harmonize"
CDE_RECOMMEND_DEFAULT_API_URL = "https://apiserver.netriasbdf.cloud/v0/cde-recommendation"


app = typer.Typer()

def harmonize(req: HarmonizationRequest,
              api_url: str,
              api_key: str,
              ssl_verify: True
              ):
    
    request_headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
        }

    # print(req.model_dump())

    logger.info("API URL: {}", api_url)

    try:
        res = httpx.post(api_url,
                         data=req.model_dump_json(),
                         headers=request_headers,
                         timeout=60,
                         verify=True,)

        res.raise_for_status()

    except HTTPStatusError as e:
        logger.error("Received apiserver error response ({}) from {}",
                     e.response.status_code, e.request.url)
        typer.echo(e.response.text)
        raise typer.Exit(code=1)

    except RequestError as e:
        typer.echo(f"Error: Network problem occurred while requesting {e.request.url} - {e}", err=True)
        raise typer.Exit(code=1)

    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1)

    return HarmonizationResponse(**res.json()['body'])


def cde_recommend(req: RecommendRequest,
                  api_url: str,
                  api_key: str,
                  ssl_verify: bool = True
                  ):
    
    request_headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
        }

    # print(req.model_dump())

    logger.info("API URL: {}", api_url)

    try:
        res = httpx.post(api_url,
                         data=req.model_dump_json(),
                         headers=request_headers,
                         timeout=60,
                         verify=True,)

        res.raise_for_status()

        return res.json()["body"]
        
    except HTTPStatusError as e:
        logger.error("Received apiserver error response ({}) from {}",
                     e.response.status_code, e.request.url)
        typer.echo(e.response.text)
        raise typer.Exit(code=1)

    except RequestError as e:
        typer.echo(f"Error: Network problem occurred while requesting {e.request.url} - {e}", err=True)
        raise typer.Exit(code=1)

    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1)

                  
@app.command()
def about():
    """CLI tooling for client scripting of the Netrias harmonization API
    """

    print("""
    CLI tooling for client scripting of the Netrias harmonization API

    Copyright 2024-25 Netrias LLC
    """)

              
@app.command(name="harmonize")
def harmonize_command(cde: int, variations: List[str],
              api_url: Annotated[str, typer.Option(help="URL of harmonizaton API endpoint")] = "",
              api_key: Annotated[str, typer.Option(help="API key for harmonizaton API endpoint")] = "",
              ssl_verify: bool = True,
              ):
    """Harmonize variations against a CDE

    A common data element, or CDE, is an identifier from a
    biomedical metadata ontology standard that indicates a set of permissible values.

    Variations are strings which we want to recommend matching permissible values for.
    
    This function calls the Netrias harmonization API endpoints to generate those recommendations.

    The following environment variables are observed by this command

    HARMONIZATION_API_URL : the API endpoint
    HARMONIZATION_API_KEY : an API key allocated by Netrias to gate and measure API usage
    """


    if not api_url:
        api_url = os.environ.get("HARMONIZATION_API_URL",
                                 HARMONIZATION_DEFAULT_API_URL)
    
    if not api_key:
        api_key = os.environ.get("HARMONIZATION_API_KEY", "")

    def build_request(variation, cde):
        return HarmonizationRequest(
            body=HarmonizationVariation(
                string_to_harmonize=variation,
                cde_id=cde,
                data_commons_id=1,
                cde_version_id="v1"
            )
        )

    requests = [build_request(variation, cde) for variation in variations]
    
    responses = [harmonize(r, api_url, api_key, ssl_verify) for r in requests]
                 
                           
    # json.dump(harmonizations, fp=sys.stdout)
    json.dump([r.model_dump() for r in responses], fp=sys.stdout)
    # print(file=sys.stdout)

@app.command(name="cde-recommendation")
def cde_recommend_command(target_schema: Annotated[RecommendSchema, typer.Argument()],
                          input_file: Annotated[typer.FileText, typer.Argument()],
                          api_url: Annotated[str, typer.Option(help="URL of harmonizaton API endpoint")] = "",
                          api_key: Annotated[str, typer.Option(help="API key for harmonizaton API endpoint")] = "",
                          ssl_verify: bool = True,
                          ):

    """Recommend CDEs to harmonize tabular data

    A common data element, or CDE, is an identifier from a
    biomedical metadata ontology standard that indicates a set of permissible values.

    In tabular data, for each column we want to recommend a CDE that
    is most suitable for harmonizing each row of that column. A given
    table may have multiple differeng applicable CDEs dependent on the
    data inthe columns.
    
    This function calls the Netrias harmonization API endpoints to generate those recommendations.

    The following environment variables are observed by this command

    CDE_RECOMMEND_API_URL : the API endpoint
    HARMONIZATION_API_KEY : an API key allocated by Netrias to gate and measure API usage
    """
    
    if not api_url:
        api_url = os.environ.get("CDE_RECOMMEND_API_URL",
                                 CDE_RECOMMEND_DEFAULT_API_URL)
    
    if not api_key:
        api_key = os.environ.get("HARMONIZATION_API_KEY", "")

    def build_request(target_schema, input_file):
        json_columns = json.load(fp=input_file)
        req_table = HarmonizationTable(target_schema=target_schema,
                                       data=json_columns)
        req = RecommendRequest(body=req_table)
        return req


    logger.info("Generating cde recommendations via schema {} for tabular data from: {}",
                target_schema, input_file.name)
    req = build_request(target_schema, input_file)
    # logger.info("RecommendRequest: {}", req)

    res = cde_recommend(req, api_url, api_key)
    sys.stdout.write(res)

def main() -> None:
    load_dotenv()
    app()

