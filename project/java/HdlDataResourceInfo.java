package None;

import java.util.List;
import lombok.*;






/**
  The data element in the handle API for the resource info.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataResourceInfo  {

  private String format;
  private ResourceInfo value;

}
