package None;

import java.util.List;
import lombok.*;






/**
  The data class for the schema version.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataSchemaVer  {

  private String format;
  private String value;

}
