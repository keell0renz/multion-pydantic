from pydantic import BaseModel, Field, ValidationError, field_validator
from multion.client import MultiOn
from multion.types.retrieve_output import RetrieveOutput

class MultiOnPydantic:  # Used during MultiOn() object assignment to provide type hinting.
    def retrieve_with_model(self, *args, **kwargs) -> RetrieveOutput | BaseModel:
        raise NotImplementedError()

def retrieve_with_model(
    self, output_schema: BaseModel | None = None, *args, **kwargs
) -> RetrieveOutput | BaseModel:

    if output_schema:
        schema = output_schema.model_json_schema()

        # Parse for field names and their respective types, description, examples.
        fields: list[tuple[str, str, str, str]] = [
            (
                name,
                field["type"],
                field.get("description", "No description provided."),
                field.get("examples", ["No example provided."])[0],
            )
            for name, field in schema["properties"].items()
        ]

        # Pass docstring as main body of cmd and attach field names and their respective types.
        cmd = f"{output_schema.__doc__}\nPlease ensure proper typing of the outputs:\n{fields}"

        # Create arguments list based on schema.
        args_list = list(output_schema.model_json_schema()["required"])

        # Call to original Retrieval API.
        response = self.retrieve(cmd=cmd, fields=args_list, *args, **kwargs)

        # Schema is constructed and validated.
        try:
            return output_schema.model_validate(response.data[0])
        except ValidationError as e:
            # TODO Handle potential re-request to model to fix the error.
            raise ValidationError() from e

    return self.retrieve(*args, **kwargs)  # API call in case output_schema is not used.

# A little pythonic trick to modify existing code without editing the source code.
setattr(MultiOn, "retrieve_with_model", retrieve_with_model)
