package None;

import java.util.List;
import lombok.*;






/**
  The data element in the handle API for the schema version.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class LICENSE extends HandleRecord {

  private Integer index;
  private HdlDataLicense data;

}
